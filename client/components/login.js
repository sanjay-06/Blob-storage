import { useState } from "react";

const Login = () => {

        const [state, setState] = useState({
          email: "",
          password: ""
        });

        function handleChange(e) {
            console.log(e.target)
            setState({ ...state, [e.target.name]: e.target.value });
        }

        async function handleSubmit(e) {
          e.preventDefault();

          const res = fetch(`http://localhost:8000/hello`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              formData: {email: state.email , password:state.password}
            })
          })
          let resp=await res
          if(resp.status == 200)
          {
            window.location.href="/files"
          }
          else if(resp.status == 404)
          {
            document.getElementById("email").className="block w-full px-4 py-3 mb-4 border-2 border-transparent border-red-200 rounded-lg focus:ring focus:ring-blue-500 focus:outline-none"
            document.getElementById("password").className="block w-full px-4 py-3 mb-4 border-2 border-transparent border-red-200 rounded-lg focus:ring focus:ring-blue-500 focus:outline-none"
            document.getElementById("us").className="text-md text-red-200"
            document.getElementById("pass").className="text-md text-red-200"
          }

        }

  return(
    <section className="w-full px-8 mt-44 bg-white xl:px-8">
        <div className="max-w-5xl mx-auto">
            <div className="flex flex-col items-center md:flex-row">
                <div className="w-full space-y-5 md:w-3/5 md:pr-16">
                <p className="font-medium text-blue-500 uppercase">
                    Building Businesses
                </p>
                <h2 className="text-2xl font-extrabold leading-none text-black sm:text-3xl md:text-5xl">
                    Changing The Way People Do Business.
                </h2>
                <p className="text-xl text-gray-600 md:pr-16">
                    Learn how to engage with your visitors and teach them about your
                    mission. We're revolutionizing the way customers and businesses
                    interact.
                </p>
                </div>
                <div className="w-full mt-16 md:mt-0 md:w-2/5">
                <div className="relative z-10 h-auto p-8 py-10 overflow-hidden bg-white border-b-2 border-gray-300 rounded-lg shadow-2xl px-7">
                    <h3 className="mb-6 text-2xl font-medium text-center">
                    Sign in to your Account
                    </h3>
                    <form onSubmit={handleSubmit}>
                        <input
                        type="text"
                        name="email"
                        className="block w-full px-4 py-3 mb-4 border-2 border-transparent border-gray-200 rounded-lg focus:ring focus:ring-blue-500 focus:outline-none"
                        placeholder="Email address"
                        onChange={handleChange}
                        value={state.email}
                        id="email"
                        required
                        />
                        <h1 className="hidden" id="us">Invalid user</h1>
                        <input
                        type="password"
                        name="password"
                        id="password"
                        className="block w-full px-4 py-3 mb-4 border-2 border-transparent border-gray-200 rounded-lg focus:ring focus:ring-blue-500 focus:outline-none"
                        placeholder="Password"
                        onChange={handleChange}
                        value={state.password}
                        required
                        />
                        <h1 className="hidden" id="pass"> Invalid password</h1>

                        <div className="block">
                            <button className="w-full px-3 py-4 font-medium text-white bg-blue-600 rounded-lg"
                                type="submit"
                            >
                                    Log Me In

                            </button>
                    </div>
                    </form>
                    <p className="w-full mt-4 text-sm text-center text-gray-500">
                    Don't have an account?{" "}
                    <a href="/signup" className="text-blue-500 underline">
                        Sign up here
                    </a>
                    </p>
                </div>
                </div>
            </div>
        </div>
  </section>
  )
};

export default Login