import React, { useMemo, useCallback } from "react";
import {
  createColumnHelper,
  tableFeatures,
  rowPaginationFeature,
  createPaginatedRowModel,
  useTable,
  metaHelper,
} from "@tanstack/react-table";
import { Table as BTable } from "react-bootstrap";

import { useSearch } from "../context/searchContext";
import Checkbox from "../components/checkbox";
import SearchInput from "../components/search-input";
import { CATEGORIES } from "../types";
import type { Result } from "../types";

import "./search.css";

interface ColumnMeta {
  className?: string;
}

const features = tableFeatures({
  rowPaginationFeature,
  paginatedRowModel: createPaginatedRowModel(),
  columnMeta: metaHelper<ColumnMeta>(),
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
      initialState: { pagination: { pageIndex: 0, pageSize: 25 } },
      debugTable: false,
    },
    (state) => state, // default selector
  );
  return (
    <div>
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
      <BTable striped hover responsive>
        <tbody>
          {table.getRowModel().rows.map((row) => {
            return (
              <tr key={row.id} onClick={() => console.log(row.original.link)}>
                {row.getAllCells().map((cell) => {
                  return (
                    <td
                      key={cell.id}
                      className={cell.column.columnDef.meta?.className ?? ""}
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
    handleCategoryAndSearch,
    handleSearch,
    handleQueryChange,
    categories,
    results,
    query,
    searchedQuery,
  } = useSearch();

  const onSubmit = useCallback(
    (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      handleSearch();
    },
    [handleSearch],
  );

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
      <form className="explore-form" onSubmit={onSubmit}>
        <div className="form-group row">
          <div className="col col-md-2"></div>
          <div className="col col-md-8">
            <div className="input-group query-input-group">
              <SearchInput
                onInputChange={handleQueryChange}
                placeholder="Search"
                submitValue="Apply Filter"
                showSubmitButton={true}
                value={query}
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
                onChange={() => handleCategoryAndSearch(category)}
              />
            </div>
          ))}
        </div>
      </form>
      <div className="row content-row">
        <div className="col col-md-8 results-left ">
          <div className="row justify-content-center">
            <div className="col-auto px-4 results-control-left">
              <span>
                Results: {results.length}
                <i>
                  {searchedQuery
                    ? ` Results for "${searchedQuery}"`
                    : " Results"}
                </i>
              </span>
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
