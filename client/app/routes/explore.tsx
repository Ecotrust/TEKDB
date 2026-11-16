import React, {useEffect} from "react";
import { useSearch } from "../context/searchContext";
import Checkbox from "../components/checkbox";
import SearchInput from "../components/search-input";
import { CATEGORIES } from "../types";

import "./explore.css";

const ExploreRoute: React.FC = () => {
  const {
    handleCategoryTypeChange,
    handleSearch,
    handleQueryChange,
    categories,
  } = useSearch();

  // clear the search query on component mount
  useEffect(() => {
    handleQueryChange("");
  }, [])

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    handleSearch();
  };

  return (
    <div className="container-fluid">
      <div className="row content-row">
        <div className="col well content-well accent-bg">
          <section className="container">
            <div className="explore-form-row row min-full-height">
              <div className="col form-wrapper">
                <form className="explore-form" onSubmit={onSubmit}>
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

                  <div className=" explore-input-group">
                    <SearchInput
                      onInputChange={handleQueryChange}
                      placeholder="Search"
                      submitValue="GO"
                      showSubmitButton={false}
                    />
                  </div>
                  <div
                    className="row"
                    id="filter-checkboxes"
                    aria-label="category-type-selection"
                  >
                    <div className="col-12 col-xl-2" role="category-group">
                      <p>Categories:</p>
                    </div>
                    {CATEGORIES.map((category) => (
                      <div className="col-lg-2 col-xl-2" role="category-group" key={category}>
                        <Checkbox
                          label={category}
                          checked={categories.includes(category)}
                          onChange={() => handleCategoryTypeChange(category)}
                        />
                      </div>
                    ))}
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
