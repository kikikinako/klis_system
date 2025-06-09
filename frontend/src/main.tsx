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
import Index from "./pages/index";
import Search_title from "./pages/search_title";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route
    path="/"
    element={<Root />}
    errorElement={<ErrorPage />}>
      <Route index element={<Index />} />
      <Route
      path="search_title"
      element={<Search_title />}/>
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
