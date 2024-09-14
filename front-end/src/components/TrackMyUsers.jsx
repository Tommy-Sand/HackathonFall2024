import React, { useState } from 'react';
import Filter from './Filter';  
import UserList from './List';
import AddUserForm from './AddUser';
import './TrackMyUsers.css'

function TrackMyUsers() {
  const [applications, setUsers] = useState([
    { id: 1, company: 'Joel', position: 'Developer', dateApplied: '2024-09-10', status: 'Applied' },
    { id: 2, company: 'Haoze', position: 'TA', dateApplied: '2024-08-25', status: 'Interview' },
  ]);


  const [filterStatus, setFilterStatus] = useState('All');

  const [newUser, setNewUser] = useState({
    company: '', position: '', dateApplied: '', status: 'Applied',
  });


  function addUser() {
    const newApp = { ...newUser, id: applications.length + 1 };
    setUsers(applications.concat(newApp));
    setNewUser({ company: '', position: '', dateApplied: '', status: 'Applied' });
  }


  function deleteUser(id) {
    const updatedUsers = applications.filter(function(app) {
      return app.id !== id;
    });
    setUsers(updatedUsers);
  }

  function signInUser(id) {
    // go to applications page
  }


  return (
    <div className = "track-applications">
      <h2>Select User</h2>
    
      {/* <Filter filterStatus={filterStatus} setFilterStatus={setFilterStatus} /> */}
      <UserList applications={filteredUsers} deleteUser={deleteUser} />
      <AddUserForm
        newUser={newUser}
        setNewUser={setNewUser}
        addUser={addUser}
      />
    </div>
  );
}
export default TrackMyUsers;
