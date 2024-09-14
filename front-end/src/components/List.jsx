import './List.css'
function UserList({ applications, deleteUser, signInUser }) {
    return (
      <ul className = "list">
        {applications.map(app => (
          <li key={app.id} className = "application-item">
            {app.company}
            <button onClick={() => signInUser(app.id)}>Sign In</button>
            <button onClick={() => deleteUser(app.id)}>Delete</button>
          </li>
        ))}
      </ul>
    );
  }
  
  export default UserList;