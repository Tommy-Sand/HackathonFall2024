import React, { useState } from 'react';
import './ResumeManager.css';

function EditMasterResume({ masterResume, setMasterResume }) {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setMasterResume({ ...masterResume, [name]: value });
  };

  return (
    <div>
      <h2>Edit Master Resume</h2>
      <form>
        <textarea
          name="resumeText"
          value={masterResume.resumeText}
          onChange={handleChange}
          placeholder="Enter your resume here"
          rows="10"
          cols="50"
        />
      </form>
    </div>
  );
}

function EditTailoredResume({ resume, setResume }) {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setResume({ ...resume, [name]: value });
  };

  return (
    <div>
      {resume.editable ? (
        <form>
          <div className="resume-form">
            <input
              type="text"
              name="title"
              value={resume.title}
              onChange={handleChange}
              placeholder="Title"
            />
            <textarea
              name="resumeText"
              value={resume.resumeText}
              onChange={handleChange}
              placeholder="Edit your resume for this application"
              rows="10"
              cols="50"
            />
          </div>
          <button onClick={() => setResume({ ...resume, editable: false })}>Save</button>
        </form>
      ) : (
        <div>
          <p>{resume.resumeText}</p>
        </div>
      )}
    </div>
  );
}


function ResumeManager() {
  const [masterResume, setMasterResume] = useState({
    resumeText: ''
  });

  const [tailoredResumes, setTailoredResumes] = useState([]);

  function createTailoredResume() {
    const newResume = { ...masterResume, id: tailoredResumes.length + 1, title: '', editable: true };
    setTailoredResumes(tailoredResumes.concat(newResume));
  }

  return (
    <div>
      <EditMasterResume masterResume={masterResume} setMasterResume={setMasterResume} />
      <button onClick={createTailoredResume}>Create Tailored Resume</button>
      <div className="tailored-resumes">
        {tailoredResumes.map((resume) => (
          <div key={resume.id} className="resume-icon">
            <h3>{resume.title || 'Untitled'}</h3>
            <button onClick={() => setTailoredResumes(tailoredResumes.filter(r => r.id !== resume.id))}>Delete</button>
            <EditTailoredResume resume={resume} setResume={(updatedResume) => {
              setTailoredResumes(tailoredResumes.map(r => r.id === resume.id ? updatedResume : r));
            }} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default ResumeManager;