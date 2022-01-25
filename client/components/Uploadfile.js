import { useState } from "react";
import Select from 'react-select';
import makeAnimated from 'react-select/animated';
const animatedComponents = makeAnimated();

const UploadFile = () => {
  const [filenames, setfilename] = useState("Attach you files here");
  const [multivalues, setmultivalues] = useState([]);
  const [handletitle, sethandletitle] = useState("");

  const options = [
    { value: 'chocolate', label: 'Chocolate' },
    { value: 'strawberry', label: 'Strawberry' },
    { value: 'vanilla', label: 'Vanilla' }
  ]

  const setvalues=(e)=>{
    console.log(e)
    setmultivalues(e)
  }

  async function sendFile(frmdetails) {
    console.log(frmdetails)
    const res = fetch(`http://localhost:8000/sendFile`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        formData: frmdetails
      })
    })
    let resp=await res
    console.log(resp)
  }

  const handleSubmit=() =>{
  //  console.log(multivalues)
   const frmdetails = {
    'users' : multivalues,
    'title' : handletitle,
    'file' : filenames
  }
  console.log(frmdetails);
  sendFile(frmdetails)
  alert("File added");
  setfilename("Attach you files here")

  }

  const handleChange=()=>{
    let a=document.getElementById("filename").value
    var pattern = /\\/;
    let result = a.split( pattern );
    setfilename(
      result.pop()
    )
  }
  return(
    <div className="py-20 h-screen bg-gray-300 px-2">
    <form onSubmit={handleSubmit}>
    <div className="max-w-md mx-auto bg-white rounded-lg overflow-hidden md:max-w-lg">
      <div className="md:flex">
        <div className="w-full px-4 py-6 ">
          <div className="mb-1">
            {" "}
            <span className="text-sm">Title</span>{" "}
            <input
              type="text"
              className="h-12 px-3 w-full border-blue-400 border-2 rounded focus:outline-none focus:border-blue-600"
              onChange={(e)=>sethandletitle(e.target.value)}
              required
            />{" "}
          </div>
          <div className="mb-1 pt-4">
            {" "}
            <span className="text-sm">Add Users and their permissions</span>{" "}
            <Select
              closeMenuOnSelect={false}
              components={animatedComponents}
              isMulti
              options={options}
              className="pt-1 pb-4"
              onChange={setvalues}
            />
           {" "}
          </div>
          <div className="mb-1">
            {" "}
            <span>Attachments</span>
            <div className="relative h-32 rounded-lg border-dashed border-2 border-blue-700 bg-gray-100 flex justify-center items-center">
              <div className="absolute">
                <div className="flex flex-col items-center">
                  {" "}
                  <i className="fa fa-folder-open fa-3x text-blue-700" />{" "}
                  <span className="block text-gray-400 font-normal" id="fileadd">
                    {filenames}
                  </span>{" "}
                </div>
              </div>{" "}
              <input type="file" className="h-full w-full opacity-0" onChange={handleChange} id="filename" required/>
            </div>
          </div>
          <div className="mt-3 text-right">
            {" "}
            <button type="clear border-none">Cancel</button>{" "}
            <button type="submit" className="ml-2 h-10 w-32 bg-blue-600 rounded text-white hover:bg-blue-700">
              Create
            </button>{" "}
          </div>
        </div>
      </div>
    </div>
    </form>

  </div>

  )
};

export default UploadFile