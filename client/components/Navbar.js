import { useState } from "react"

const Navbar = () => {

  const [value,setvalue] = useState(
    'left-0 z-10 items-center justify-center w-full font-semibold select-none md:flex lg:absolute hidden'
  )

  const [sign,setsigns] = useState(
    'relative z-20 flex-col justify-center pr-5 mt-4 space-y-8 md:pr-3 lg:pr-0 md:flex-row md:space-y-0 md:items-center md:space-x-6 md:mt-0 hidden md:flex'
  )
  const [cross,setcross] = useState(
    'w-6 h-6 text-gray-700 hidden'
  )

  const [nav,setnav]=useState(
    'w-6 h-6 text-gray-700'
  )


  const handleSearch = () => {
     SetSearch(
       'block'
     )
  }
  const handleClick= () =>{

    if(value == 'left-0 z-10 items-center justify-center w-full font-semibold select-none md:flex lg:absolute hidden')
    {
      setvalue(
        'left-0 z-10 items-center justify-center w-full font-semibold select-none md:flex lg:absolute flex'
      )
      setsigns
      (
        'relative z-20 flex-col justify-center pr-5 mt-4 space-y-8 md:pr-3 lg:pr-0 md:flex-row md:space-y-0 md:items-center md:space-x-6 md:mt-0 flex'
      )
      setcross(
        'w-6 h-6 text-gray-700'
      )
      setnav(
        'w-6 h-6 text-gray-700 hidden'
      )
    }
    else
    {
      setvalue(
        'left-0 z-10 items-center justify-center w-full font-semibold select-none md:flex lg:absolute hidden'
      )
      setsigns
      (
        'relative z-20 flex-col justify-center pr-5 mt-4 space-y-8 md:pr-3 lg:pr-0 md:flex-row md:space-y-0 md:items-center md:space-x-6 md:mt-0 hidden md:flex'
      )
      setcross(
        'w-6 h-6 text-gray-700 hidden'
      )
      setnav(
        'w-6 h-6 text-gray-700'
      )
    }
  }

    return(
        <section className="antialiased bg-white">
  <div className="px-12 mx-auto max-w-7xl">
  <nav
    x-data="{ mobile: false }"
    className="relative pt-6 mx-auto md:pb-6 max-w-7xl md:flex md:justify-between md:items-center"
  >
    <div className="relative z-20 flex items-center justify-between pb-5">
      <div>
        <a
          className="text-xl font-bold text-gray-800 md:text-2xl hover:text-indigo-600"
          href="#_"
        >
          Blob Server.
        </a>
      </div>
      {/* Mobile menu button */}
      <div className="flex md:hidden">
        <button
          type="button"
          className="text-gray-500 hover:text-indigo-600"
          aria-label="toggle menu"
          onClick={handleClick}
        >
          <svg
          className={nav}
          x-show="!showMenu"
          fill="none"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
        <path d="M4 6h16M4 12h16M4 18h16" />
      </svg>
      <svg
        className={cross}
        x-show="showMenu"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M6 18L18 6M6 6l12 12"
        />
      </svg>
        </button>
      </div>
    </div>
    {/* Mobile Menu open: "block", Menu closed: "hidden" */}
    <div className={value}>
      <div className="flex flex-col justify-center w-full mt-4 space-y-2 md:mt-0 md:flex-row md:space-x-6 lg:space-x-10 xl:space-x-16 md:space-y-0">
        <a
          className="py-3 text-gray-800 hover:text-indigo-600"
          href="/files"
        >
        Files
        </a>
        <a
          className="py-3 text-gray-800 hover:text-indigo-600"
          href="/upload"
        >
          Upload
        </a>
        <a
          className="py-3 text-gray-800 hover:text-indigo-600"
          href="/permissions"
        >
          Permissions
        </a>

      </div>
    </div>
    <div className={sign}>
      <a
        href="/"
        className="flex-shrink-0 w-auto text-base font-semibold leading-5 text-left text-gray-800 capitalize bg-transparent md:text-sm md:py-3 md:px-8 md:font-medium md:text-center md:text-white md:bg-indigo-600  hover:bg-indigo-800 md:mx-0 md:shadow-xl rounded-2xl"
      >
        Log out
      </a>
    </div>
  </nav>
  </div>
</section>
    )
}
export default Navbar