import { Outlet, NavLink } from "react-router-dom";


export default function Root () {
  return (
    <>
      <div className="container">
        <header className="header">
          <div className="header-bg" />
          <div className="header-inner">
            <NavLink to={""}>
              <img src="/logo.png" alt="logo" className="logo" />
            </NavLink>
            <div className="header-site-menu">
              <ul className="site-menu">
                <li>
                  <NavLink to={""} className={"link"}>
                    トップ
                  </NavLink>
                </li>
                <li>
                  <NavLink to={"search_fulltext"} className={"link"}>
                    単語検索
                  </NavLink>
                </li>
                <li>
                  <NavLink to={"search_title"} className={"link"}>
                    記事名検索
                  </NavLink>
                </li>
                <li>
                  <NavLink to={"about"} className={"link"}>
                    About
                  </NavLink>  
                </li>  
              </ul>  
            </div>
          </div>
        </header>
        <div className="content">
          <Outlet />
        </div>
      </div>
    </>
  )
}