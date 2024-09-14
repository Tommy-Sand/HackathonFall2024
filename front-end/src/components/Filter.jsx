import './Filter.css'
function Filter({ filterStatus, setFilterStatus }) {
    return (
      <div className = "filter-container">
        <label>Filter by Status: </label>
        <select value={filterStatus} onChange={e => setFilterStatus(e.target.value)}>
          <option value="All">All</option>
          <option value="Applied">Applied</option>
          <option value="Interview">Interview</option>
          <option value="Offer">Offer</option>
          <option value="Rejection">Rejection</option>
        </select>
      </div>
    );
  }
  
  export default Filter;