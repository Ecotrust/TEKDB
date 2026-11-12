import './search-input.css';

type SearchInputProps = {
  onInputChange: (query: string) => void;
  placeholder: string;
  submitValue: string;
  showSubmitButton: boolean;
  value?: string;
};

const SearchInput: React.FC<SearchInputProps> = ({
  onInputChange,
  placeholder,
  submitValue,
  showSubmitButton,
  value,
}) => {
  return (
    <div className={`input-group query-input-group${showSubmitButton ? " has-submit-button" : ""}`}>
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
        type="text"
        className="form-control"
        id="search-text"
        name="query"
        placeholder={placeholder}
        aria-describedby="search-icon-label"
        onChange={(e) => onInputChange(e.target.value)}
        value={value}
      />
      {showSubmitButton && <span className="search-arrow arrow-right"></span>}
      <input type="submit" id="query-form-submit" value={submitValue} />
    </div>
  );
};

export default SearchInput;
