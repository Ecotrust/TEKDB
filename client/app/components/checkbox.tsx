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
    <>
      <input
        type="checkbox"
        onChange={() => onChange()}
        checked={checked}
        id={`check-${label.toLowerCase()}`}
        className="checkbox-input"
      />
      <label htmlFor={`check-${label.toLowerCase()}`} className="checkbox-label"></label> {label}
    </>
  );
};

export default Checkbox;
