import type React from "react";
import { Outlet } from "react-router";
import Header from "../components/header";
import { usePageContentAndSiteInfo } from "../api/pageContent";
import { useLogin } from "../context/loginContext";

const ExploreLayout: React.FC = () => {
  const { pageContent, siteInfo } = usePageContentAndSiteInfo();
  const {loginForm} = useLogin();

  return (
    <>
      <Header
        projIcons={siteInfo?.proj_icons || { logo: "" }}
        projTextPlacement={siteInfo?.proj_text_placement || "top"}
        projLogoText={siteInfo?.proj_logo_text || ""}
        isAuthenticated={loginForm?.isAuthenticated}
        pageTitle={pageContent?.pageTitle || "Explore"}
      />
      <main className="content-wrapper">
        <Outlet context={{ pageContent, siteInfo }} />
      </main>
    </>
  );
};

export default ExploreLayout;
