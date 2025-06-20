import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createRoutesFromElements,
  createBrowserRouter,
  Route,
  RouterProvider,
} from "react-router-dom";
import "./index.css";
import Root from "./pages/root";
import ErrorPage from "./pages/error_page"
import Home from "./pages/home";
import About from "./pages/about";
import Search_title from "./pages/search_title";
import Search_fulltext from "./pages/search_fulltext";
import IrregularIssue from "./pages/irregular_issue";

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route
      path="/"
      element={<Root />}
      errorElement={<ErrorPage />}>
        <Route index element={<Home />} />
        <Route
        path="about"
        element={<About />}/>
        <Route
        path="search_fulltext"
        element={<Search_fulltext />}/>
        <Route
        path="search_title"
        element={<Search_title />}/>
        <Route
        path="irregular_issue"
        element={<IrregularIssue />} />
      </Route>
    </>
  )
);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
