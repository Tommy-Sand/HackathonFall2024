import './AddApplication.css'
function AddApplicationForm({ newApplication, setNewApplication, addApplication }) {
    return (
      <div className = "add-application-form">
        <h3>Add New Application</h3>
        <input
          type="text"
          placeholder="Company"
          value={newApplication.company}
          onChange={e => setNewApplication({ ...newApplication, company: e.target.value })}/>
        <input
          type="text"
          placeholder="Position"
          value={newApplication.position}
          onChange={e => setNewApplication({ ...newApplication, position: e.target.value })}/>
        <input
          type="date"
          value={newApplication.dateApplied}
          onChange={e => setNewApplication({ ...newApplication, dateApplied: e.target.value })}/>
        <select
          value={newApplication.status}
          onChange={e => setNewApplication({ ...newApplication, status: e.target.value })}
        >
          <option value="Applied">Applied</option>
          <option value="Interview">Interview</option>
          <option value="Offer">Offer</option>
          <option value="Rejection">Rejection</option>
        </select>
        <button onClick={addApplication}>Add Application</button>
      </div>
    );
  }
  
  export default AddApplicationForm;