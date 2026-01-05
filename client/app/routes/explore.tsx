import React, { useState } from "react";
import "./explore.css";

const ExploreRoute: React.FC = () => {
  const [categories, setCategories] = useState<string[]>([]);

  const handleCategoryTypeChange = (type: string) => {
    if (categories.includes(type)) {
      setCategories(categories.filter((category) => category !== type));
    } else {
      setCategories([...categories, type]);
    }
  };
  console.log("Selected categories:", categories);
  return (
    <div className="container-fluid content-container">
      <div className="row content-row">
        <div className="col well content-well accent-bg">
          <section className="container">
            <div className="explore-form-row row min-full-height">
              <div className="col form-wrapper">
                <form className="explore-form" method="post" action="/search/">
                  <h1>Search &amp; Browse</h1>
                  <p>
                    You can search by term alone and/or add category filters
                    below.
                    <br />
                    To see all items in a category, select checkbox(es) below
                    with no search term.
                    <br />
                    <em>
                      Leave the search bar &amp; checkboxes blank to see
                      everything available.
                    </em>
                  </p>

                  <div className="input-group explore-input-group">
                    <span className="input-group-text" id="search-icon-label">
                      <svg
                        id="Symbol_62_2"
                        data-name="Symbol 62 – 2"
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        viewBox="0 0 16 16"
                      >
                        <rect
                          id="Rectangle_176"
                          data-name="Rectangle 176"
                          width="16"
                          height="16"
                          fill="none"
                        />
                        <path
                          id="Path_99"
                          data-name="Path 99"
                          d="M15.9,14.5l-3.3-3.3A6.847,6.847,0,0,0,14,7,6.957,6.957,0,0,0,7,0,6.957,6.957,0,0,0,0,7a6.957,6.957,0,0,0,7,7,6.847,6.847,0,0,0,4.2-1.4l3.3,3.3ZM2,7A4.951,4.951,0,0,1,7,2a4.951,4.951,0,0,1,5,5,4.951,4.951,0,0,1-5,5A4.951,4.951,0,0,1,2,7Z"
                        />
                      </svg>
                    </span>
                    <input
                      type="search"
                      className="form-control"
                      id="search-text"
                      name="query"
                      placeholder="Search"
                      aria-describedby="search-icon-label"
                    />
                    <input type="submit" id="query-form-submit" value="GO" />
                  </div>

                  <input
                    type="text"
                    id="search-category-type"
                    name="category"
                    value=""
                    hidden
                  />
                  <div
                    className="row"
                    id="filter-checkboxes"
                    aria-label="category-type-selection"
                  >
                    <div className="col-12 col-xl-2" role="category-group">
                      <p>Categories:</p>
                    </div>
                    <div className="col-lg-2 col-xl-2" role="category-group">
                      <input
                        type="checkbox"
                        onChange={() => handleCategoryTypeChange("places")}
                        id="check-places"
                      />
                      <label htmlFor="check-places"></label> Places
                    </div>
                    <div className="col-lg-3 col-xl-2" role="category-group">
                      <input
                        type="checkbox"
                        onChange={() => handleCategoryTypeChange("resources")}
                        id="check-resources"
                      />
                      <label htmlFor="check-resources"></label> Resources
                    </div>
                    <div className="col-lg-3 col-xl-2" role="category-group">
                      <input
                        type="checkbox"
                        onChange={() => handleCategoryTypeChange("activities")}
                        id="check-activities"
                      />
                      <label htmlFor="check-activities"></label> Activity
                    </div>
                    <div className="col-lg-2 col-xl-2" role="category-group">
                      <input
                        type="checkbox"
                        onChange={() => handleCategoryTypeChange("sources")}
                        id="check-sources"
                      />
                      <label htmlFor="check-sources"></label> Source
                    </div>
                    <div className="col-lg-2 col-xl-2" role="category-group">
                      <input
                        type="checkbox"
                        onChange={() => handleCategoryTypeChange("media")}
                        id="check-media"
                      />
                      <label htmlFor="check-media"></label> Media
                    </div>
                  </div>

                  <div className="button-wrapper">
                    <button className="btn btn-style" type="submit">
                      Go <span className="arrow-right"></span>
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
};

export default ExploreRoute;
