import React, { useMemo, useCallback } from "react";
import {
  createColumnHelper,
  tableFeatures,
  rowPaginationFeature,
  createPaginatedRowModel,
  useTable,
} from "@tanstack/react-table";
import { Table as BTable } from "react-bootstrap";

import { useSearch } from "../context/searchContext";
import Checkbox from "../components/checkbox";
import { CATEGORIES } from "../utils/constants";
import type { Result } from "../types";

import "./search.css";

const features = tableFeatures({
  rowPaginationFeature,
  paginatedRowModel: createPaginatedRowModel(),
});

const columnHelper = createColumnHelper<typeof features, Result>();

const Table: React.FC<{ data: Result[]; columns: any[] }> = ({
  data,
  columns,
}) => {
  const table = useTable(
    {
      features,
      columns,
      data,
      initialState: { pagination: { pageIndex: 1, pageSize: 25 } },
      debugTable: false,
    },
    (state) => state, // default selector
  );
  return (
    <div>
      <BTable striped hover responsive>
        <tbody>
          {table.getRowModel().rows.map((row) => {
            return (
              <tr key={row.id} onClick={() => console.log(row.original.link)}>
                {row.getAllCells().map((cell) => {
                  return (
                    <td
                      key={cell.id}
                      className={cell.column.columnDef.meta?.className}
                    >
                      <table.FlexRender cell={cell} />
                    </td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </BTable>
      <div className="controls">
        <button
          className="demo-button demo-button-sm"
          onClick={() => table.firstPage()}
          disabled={!table.getCanPreviousPage()}
        >
          {"<<"}
        </button>
        <button
          className="demo-button demo-button-sm"
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
        >
          {"<"}
        </button>
        <button
          className="demo-button demo-button-sm"
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
        >
          {">"}
        </button>
        <button
          className="demo-button demo-button-sm"
          onClick={() => table.lastPage()}
          disabled={!table.getCanLastPage()}
        >
          {">>"}
        </button>
        <span className="inline-controls">
          <div>Page</div>
          <strong>
            {(table.state.pagination.pageIndex + 1).toLocaleString()} of{" "}
            {table.getPageCount().toLocaleString()}
          </strong>
        </span>
      </div>
    </div>
  );
};

const SearchRoute: React.FC = () => {
  const {
    handleCategoryTypeChange,
    handleSearch,
    handleQueryChange,
    categories,
    results,
    query,
  } = useSearch();

  const onSubmit = useCallback((e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    handleSearch(new FormData(e.currentTarget));
  }, []);

  const columns = useMemo(() => {
    return columnHelper.columns([
      columnHelper.accessor("category_name", {
        cell: (info) => info.getValue(),
        meta: {
          className: "category-name-col",
        },
      }),
      columnHelper.accessor("name", {
        cell: (info) => info.getValue(),
      }),
      columnHelper.accessor("description", {
        cell: (info) => (
          <span dangerouslySetInnerHTML={{ __html: info.getValue() }}></span>
        ),
      }),
      columnHelper.accessor("headline", {
        cell: (info) => (
          <span dangerouslySetInnerHTML={{ __html: info.getValue() }}></span>
        ),
      }),
    ]);
  }, []);

  return (
    <div className="container content-container">
      <form className="explore-form" onSubmit={onSubmit} id="filter-form">
        <div className="form-group row">
          <div className="col col-md-2"></div>
          <div className="col col-md-8">
            <div className="input-group query-input-group">
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
              <span className="search-arrow arrow-right"></span>
              <input
                type="submit"
                id="query-form-submit"
                value="Apply Filter"
              />
            </div>
          </div>
          <div className="col col-md-2"></div>
        </div>
        <div className="row content-row" id="filter-checkboxes">
          <div className="col col-md-2">
            <p>Filter By:</p>
          </div>
          {CATEGORIES.map((category) => (
            <div className="col col-md-2" key={category}>
              <Checkbox
                label={category}
                checked={categories.includes(category)}
                onChange={() => handleCategoryTypeChange(category)}
              />
            </div>
          ))}
        </div>
      </form>
      <div className="row content-row">
        <div className="row justify-content-center">
          <div className="col col-md-8 results-left">
            <div className="col-auto px-4 results-control-left">
              <span>
                Results: {results.length}
                <i>{query ? ` Results for "${query}"` : " Results"}</i>
              </span>
            </div>
            <div className="col-auto px-3 results-controls-center">
              <div id="page-controls"></div>
            </div>
            <div className="col-auto px-4 results-controls-right">
              <div id="export-links">
                <span>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="12"
                    height="14.571"
                    viewBox="0 0 12 14.571"
                  >
                    <path
                      id="Icon_material-file-download"
                      data-name="Icon material-file-download"
                      d="M19.5,9.643H16.071V4.5H10.929V9.643H7.5l6,6Zm-12,7.714v1.714h12V17.357Z"
                      transform="translate(-7.5 -4.5)"
                    />
                  </svg>
                </span>
                <a>.csv</a>|<a>.xlsx</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col">
          <Table data={results} columns={columns} />
        </div>
      </div>
    </div>
  );
};

export default SearchRoute;
