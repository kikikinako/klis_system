import { Outlet, NavLink } from "react-router-dom";


export default function Root () {
  return (
    <>
      <div className="container">
        <div className="sidebar">
          <ul className="linklist">
            <li className="link">
              <NavLink to={"home"}>
                Home
              </NavLink>
            </li>
            <li className="link">
              <NavLink to={"search_title"}>
                Search
              </NavLink>
            </li>
            <li className="link">
              <NavLink to={"about"}>
                About
              </NavLink>  
            </li>  
          </ul>  
        </div>
        <div className="content">
          <Outlet />
        </div>
      </div>
    </>
  )
}