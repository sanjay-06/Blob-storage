import React from "react";
// import { saveAs } from "file-saver";

const FileList=()=> {
//   const saveFile = () => {
//     saveAs(
//       "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
//       "example.pdf"
//     );
//   };
  return (
    <div>
      {/* <button onClick={saveFile}>download</button> */}
      <div className="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5">
  {/*Card 1*/}
  <div className="rounded overflow-hidden shadow-lg">
    <img className="ml-40 w-36 h-36" src="file.png" alt="Mountain" />
    <div className="px-6 py-4">
      <div className="font-bold text-xl mb-2">Mountain</div>
      <p className="text-gray-700 text-base pb-5">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus
        quia, Nonea! Maiores et perferendis eaque, exercitationem praesentium
        nihil.
      </p>
    </div>
    <div className="p-10 border-t-2 border-gray-100">
        <div className="flex flex-col items-center justify-center">
            <button className="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
                <svg className="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
                <span>Download</span>
            </button>
        </div>
    </div>
  </div>
  {/*Card 2*/}
  <div className="rounded overflow-hidden shadow-lg">
    <img className="ml-40 w-36 h-36" src="file.png" alt="Mountain" />
    <div className="px-6 py-4">
      <div className="font-bold text-xl mb-2">Mountain</div>
      <p className="text-gray-700 text-base pb-5">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus
        quia, Nonea! Maiores et perferendis eaque, exercitationem praesentium
        nihil.
      </p>
    </div>
    <div className="p-10 border-t-2 border-gray-100">
        <div className="flex flex-col items-center justify-center">
            <button className="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
                <svg className="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
                <span>Download</span>
            </button>
        </div>
    </div>
  </div>
  {/*Card 3*/}
  <div className="rounded overflow-hidden shadow-lg">
    <img className="ml-40 w-36 h-36" src="file.png" alt="Mountain" />
    <div className="px-6 py-4">
      <div className="font-bold text-xl mb-2">Mountain</div>
      <p className="text-gray-700 text-base pb-5">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus
        quia, Nonea! Maiores et perferendis eaque, exercitationem praesentium
        nihil.
      </p>
    </div>
    <div className="p-10 border-t-2 border-gray-100">
        <div className="flex flex-col items-center justify-center">
            <button className="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
                <svg className="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
                <span>Download</span>
            </button>
        </div>
    </div>
  </div>
</div>


    </div>

  );
}
export default FileList