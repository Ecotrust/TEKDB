const Checkbox = ({
  label,
  onChange,
  checked,
}: {
  label: string;
  onChange: () => void;
  checked: boolean;
}) => {
  return (
    <div className="col-lg-2 col-xl-2" role="category-group">
      <input
        type="checkbox"
        onChange={() => onChange()}
        checked={checked}
        id={`check-${label.toLowerCase()}`}
      />
      <label htmlFor={`check-${label.toLowerCase()}`}></label> {label}
    </div>
  );
};

export default Checkbox;
