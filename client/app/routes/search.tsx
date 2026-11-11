import React from "react";
import { useSearch } from "../context/searchContext";
import Checkbox from "../components/checkbox";
import { CATEGORIES } from "../utils/constants";

const SearchRoute: React.FC = () => {
  const {
    handleCategoryTypeChange,
    handleSearch,
    handleQueryChange,
    categories,
    results,
    query,
  } = useSearch();

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    handleSearch(new FormData(e.currentTarget));
  };
  return (
    <div>
      <form className="query-form" onSubmit={onSubmit} id="filter-form">
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
              onChange={(e) => handleQueryChange(e.target.value)}
              value={query}
            />
            <input type="submit" id="query-form-submit" value="GO" />
          </div>
          <div className="col col-md-2"></div>
        </div>
        <div className="row content-row" id="filter-checkboxes">
          <div className="col col-md-2">
            <p>Filter By:</p>
          </div>
          {CATEGORIES.map((category) => (
            <Checkbox
              key={category}
              label={category}
              checked={categories.includes(category)}
              onChange={() => handleCategoryTypeChange(category)}
            />
          ))}
        </div>
      </form>
    </div>
  );
};

export default SearchRoute;
