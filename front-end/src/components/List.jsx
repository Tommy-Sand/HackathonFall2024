import './List.css'
function ApplicationList({ applications, deleteApplication }) {
    return (
      <ul className = "list">
        {applications.map(app => (
          <li key={app.id} className = "application-item">
            {app.company} - {app.position} (Applied on: {app.dateApplied}, Status: {app.status})
            <button onClick={() => deleteApplication(app.id)}>Delete</button>
          </li>
        ))}
      </ul>
    );
  }
  
  export default ApplicationList;