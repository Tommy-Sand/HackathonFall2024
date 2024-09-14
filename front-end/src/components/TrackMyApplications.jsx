import React, { useState } from 'react';
import Filter from './Filter';  
import ApplicationList from './List';
import AddApplicationForm from './AddApplication';
import './TrackMyApplications.css'

function TrackMyApplications() {
  const [applications, setApplications] = useState([
    { id: 1, company: 'Google', position: 'Developer', dateApplied: '2024-09-10', status: 'Applied' },
    { id: 2, company: 'UofA', position: 'TA', dateApplied: '2024-08-25', status: 'Interview' },
  ]);


  const [filterStatus, setFilterStatus] = useState('All');

  const [newApplication, setNewApplication] = useState({
    company: '', position: '', dateApplied: '', status: 'Applied',
  });


  function addApplication() {
    const newApp = { ...newApplication, id: applications.length + 1 };
    setApplications(applications.concat(newApp));
    setNewApplication({ company: '', position: '', dateApplied: '', status: 'Applied' });
  }


  function deleteApplication(id) {
    const updatedApplications = applications.filter(function(app) {
      return app.id !== id;
    });
    setApplications(updatedApplications);
  }

  const filteredApplications = filterStatus === 'All'
    ? applications
    : applications.filter(function(app) {
        return app.status === filterStatus;
      });

  return (
    <div className = "track-applications">
      <h2>Track My Applications</h2>
    
      <Filter filterStatus={filterStatus} setFilterStatus={setFilterStatus} />
      <ApplicationList applications={filteredApplications} deleteApplication={deleteApplication} />
      <AddApplicationForm
        newApplication={newApplication}
        setNewApplication={setNewApplication}
        addApplication={addApplication}
      />
    </div>
  );
}
export default TrackMyApplications;
