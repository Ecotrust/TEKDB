import { usePageContentAndSiteInfo } from "../api/pageContent";
import { useLogin } from "../context/loginContext";

const WelcomePage: React.FC = () => {
  const { pageContent, siteInfo } = usePageContentAndSiteInfo();
  const { loginForm, setShowLoginModal } = useLogin();
  const isAuthenticated = loginForm.isAuthenticated;

  return (
    <div className="container">
      <div className="row gx-4 align-items-center">
        <div className="col-lg-5 homepage-column" id="homepage-left-column">
          <div
            className="welcome-content-wrapper"
            dangerouslySetInnerHTML={{ __html: pageContent?.pageContent || "" }}
          ></div>
          <div className="welcome-login-button-wrapper">
            {!isAuthenticated ? (
              <button
                type="button"
                className="btn welcome-login-btn"
                onClick={() => setShowLoginModal(true)}
              >
                Login <span className="arrow-right"></span>
              </button>
            ) : (
              <a
                href="/explore"
                type="button"
                className="btn welcome-login-btn"
              >
                Explore <span className="arrow-right"></span>
              </a>
            )}
          </div>
        </div>
        <div className="col-lg-7 homepage-column" id="homepage-right-column">
          <div className="proj-image-select-wrapper">
            <img
              src={`http://127.0.0.1:8000${siteInfo?.proj_image_select || ""}`}
              alt="project image"
            ></img>
          </div>
          {siteInfo && siteInfo.home_image_attribution && (
            <div id="proj-image-attribution">
              <a
                className="attribution-toggle"
                data-bs-toggle="collapse"
                href="#collapseAttribution"
                role="button"
                aria-expanded="false"
                aria-controls="collapseAttribution"
              >
                <i className="bi bi-info-circle"></i>
              </a>
              <div className="collapse" id="collapseAttribution">
                <p>{siteInfo.home_image_attribution}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default WelcomePage;
