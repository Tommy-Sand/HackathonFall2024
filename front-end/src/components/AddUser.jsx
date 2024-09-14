import './AddUser.css'
function AddUserForm({ newUser, setNewUser, addUser }) {
    return (
      <div className = "add-application-form">
        <h3>Add New User</h3>
        <input
          type="text"
          placeholder="Name"
          value={newUser.company}
          onChange={e => setNewUser({ ...newUser, company: e.target.value })}/>
        {/* <input
          type="text"
          placeholder="Position"
          value={newUser.position}
          onChange={e => setNewUser({ ...newUser, position: e.target.value })}/>
        <input
          type="date"
          value={newUser.dateApplied}
          onChange={e => setNewUser({ ...newUser, dateApplied: e.target.value })}/> */}
        {/* <select
          value={newUser.status}
          onChange={e => setNewUser({ ...newUser, status: e.target.value })}
        >
          <option value="Applied">Applied</option>
          <option value="Interview">Interview</option>
          <option value="Offer">Offer</option>
          <option value="Rejection">Rejection</option>
        </select> */}
        <button onClick={addUser}>Create New User</button>
      </div>
    );
  }
  
  export default AddUserForm;