const Signup = () => {
  return(
    <div className="bg-gray-200 min-h-screen flex flex-col">
    <div className="container max-w-sm mx-auto flex-1 flex flex-col items-center justify-center px-2">
      <div className="bg-white px-6 py-8 rounded shadow-md text-black w-full">
        <h1 className="mb-8 text-3xl text-center">Sign up</h1>
        <input
          type="text"
          className="block border border-grey-light w-full p-3 rounded mb-4"
          name="email"
          placeholder="Email"
        />
        <input
          type="password"
          className="block border border-grey-light w-full p-3 rounded mb-4"
          name="password"
          placeholder="Password"
        />
        <input
          type="password"
          className="block border border-grey-light w-full p-3 rounded mb-4"
          name="confirm_password"
          placeholder="Confirm Password"
        />
        <button
          type="submit"
          className="w-full text-center py-3 rounded bg-blue-500 text-white hover:bg-green-dark focus:outline-none my-1"
        >
          Create Account
        </button>
      </div>
      <div className="text-grey-dark mt-6">
        <a
          href="/"
        >
        Already have an account?
          {" "}Sign in
        </a>
        .
      </div>
    </div>
  </div>

  )
};

export default Signup