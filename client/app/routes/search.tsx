import React, { useState } from "react";


const SearchRoute: React.FC = () => {
const [categories, setCategories] = useState<string[]>([]);

  const handleCategoryTypeChange = (type: string) => {
    if (categories.includes(type)) {
      setCategories(categories.filter((category) => category !== type));
    } else {
      setCategories([...categories, type]);
    }
  };
  return (
    <div>
      <form className="query-form" method='post' action='/search/' id="filter-form">
    <div className="form-group row">
      <div className="col col-md-2"></div>
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
      <div className="col col-md-2"></div>
    </div>
    <div className="row content-row"  id="filter-checkboxes">
      <div className="col col-md-2">
        <p>
          Filter By: 
        </p>
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
  </form>
    </div>
  );
};

export default SearchRoute;