import './checkbox.css';

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
    <span className="checkbox-control">
      <input
        type="checkbox"
        onChange={() => onChange()}
        checked={checked}
        aria-label={label}
        id={`check-${label.toLowerCase()}`}
        className="checkbox-input"
      />
      <label htmlFor={`check-${label.toLowerCase()}`} className="checkbox-label"></label> {label}
    </span>
  );
};

export default Checkbox;
