import React from "react";
const Dashboard = () => {
  return (
    <div>
      <header className="header" data-header>
        <div className="container">
          <h1>
            <a href="/index.html" className="logo">
              Dashboard
            </a>
          </h1>
          <button
            className="menu-toggle-btn icon-box"
            data-menu-toggle-btn
            aria-label="Toggle Menu"
          >
            <span className="material-symbols-rounded icon">menu</span>
          </button>
          <nav className="navbar">
            <div className="container">
              <ul className="navbar-list">
                <li className="setting">
                  <span className="setting"></span>
                </li>
              </ul>
              <ul className="user-action-list">
                <li>
                  <a href="#" className="notification icon-box">
                    <span className="material-symbols-rounded icon">
                      notifications
                    </span>
                  </a>
                </li>
                <li>
                  <a href="#" className="header-profile">
                    <figure className="profile-avatar">
                      <img
                        src="Screenshot 2024-10-12 004139.png"
                        alt="Elizabeth Foster"
                        width="32"
                        height="32"
                      />
                    </figure>
                    <div>
                      <p className="profile-title">Aayush Belamkar</p>
                      <p className="profile-subtitle">Admin</p>
                    </div>
                  </a>
                </li>
              </ul>
            </div>
          </nav>
        </div>
      </header>
      <main>
        <article className="container article">
          <h2 className="h2 article-title">Hi AAYUSH</h2>
          <p className="article-subtitle">Welcome to Dashboard!</p>
          <section className="home">
            <div className="card profile-card">
              <button
                className="card-menu-btn icon-box"
                aria-label="More"
                data-menu-btn
              >
                <span className="material-symbols-rounded icon">
                  more_horiz
                </span>
              </button>
              <ul className="ctx-menu">
                <li className="ctx-item">
                  <button className="ctx-menu-btn icon-box">
                    <span
                      className="material-symbols-rounded icon"
                      aria-hidden="true"
                    >
                      edit
                    </span>
                    <span className="ctx-menu-text">Edit</span>
                  </button>
                </li>
                <li className="ctx-item">
                  <button className="ctx-menu-btn icon-box">
                    <span
                      className="material-symbols-rounded icon"
                      aria-hidden="true"
                    >
                      cached
                    </span>
                    <span className="ctx-menu-text">Refresh</span>
                  </button>
                </li>
                <li className="divider"></li>
                <li className="ctx-item">
                  <button className="ctx-menu-btn red icon-box">
                    <span
                      className="material-symbols-rounded icon"
                      aria-hidden="true"
                    >
                      delete
                    </span>
                    <span className="ctx-menu-text">Deactivate</span>
                  </button>
                </li>
              </ul>
              <div className="profile-card-wrapper">
                <figure className="card-avatar">
                  <img
                    src="Screenshot 2024-10-12 004139.png"
                    alt="Aayush Belamkar"
                    width="48"
                    height="48"
                  />
                </figure>
                <div>
                  <p className="card-title">Aayush Belamkar</p>
                  <p className="card-subtitle">Student / Graphic Designer</p>
                </div>
              </div>
              <ul className="contact-list">
                <li>
                  <a
                    href="mailto:xyz@mail.com"
                    className="contact-link icon-box"
                  >
                    <span className="material-symbols-rounded icon">mail</span>
                    <p className="text">aayushbelamkar@2005gmail.com</p>
                  </a>
                </li>
                <li>
                  <a href="tel:00123456789" className="contact-link icon-box">
                    <span className="material-symbols-rounded icon">call</span>
                    <p className="text">9321625834</p>
                  </a>
                </li>
              </ul>
              <div className="divider card-divider"></div>
              <ul className="progress-list">
                <li className="progress-item">
                  <div className="progress-label">
                    <p className="progress-title">Task Completion</p>
                    <data className="progress-data" value="85">
                      85%
                    </data>
                  </div>
                  <div className="progress-bar">
                    <div
                      className="progress"
                      style={{ "--width": "85%", "--bg": "var(--blue-ryb)" }}
                    ></div>
                  </div>
                </li>
                <li className="progress-item">
                  <div className="progress-label">
                    <p className="progress-title">Wellness Rating</p>
                    <data className="progress-data" value="7.5">
                      7.5
                    </data>
                  </div>
                  <div className="progress-bar">
                    <div
                      className="progress"
                      style={{ "--width": "75%", "--bg": "var(--coral)" }}
                    ></div>
                  </div>
                </li>
              </ul>
            </div>
            <div className="card-wrapper">
              <div className="card task-card">
                <div className="card-icon icon-box green">
                  <span className="material-symbols-rounded icon">
                    task_alt
                  </span>
                </div>
                <div>
                  <data className="card-data" value="21">
                    21
                  </data>
                  <p className="card-text">Calender Tasks Completed</p>
                </div>
              </div>
              <div className="card task-card">
                <div className="card-icon icon-box blue">
                  <span className="material-symbols-rounded icon">
                    drive_file_rename_outline
                  </span>
                </div>
                <div>
                  <data className="card-data" value="13">
                    13
                  </data>
                  <p className="card-text">Calender Tasks Inprogress</p>
                </div>
              </div>
            </div>
            <div className="card revenue-card">
              <button
                className="card-menu-btn icon-box"
                aria-label="More"
                data-menu-btn
              >
                <span className="material-symbols-rounded icon">
                  more_horiz
                </span>
              </button>
              <ul className="ctx-menu">
                <li className="ctx-item">
                  <button className="ctx-menu-btn icon-box">
                    <span
                      className="material-symbols-rounded icon"
                      aria-hidden="true"
                    >
                      edit
                    </span>
                    <span className="ctx-menu-text">Edit</span>
                  </button>
                </li>
                <li className="ctx-item">
                  <button className="ctx-menu-btn icon-box">
                    <span
                      className="material-symbols-rounded icon"
                      aria-hidden="true"
                    >
                      cached
                    </span>
                    <span className="ctx-menu-text">Refresh</span>
                  </button>
                </li>
              </ul>
              <p className="card-title">Income</p>
              <data className="card-price" value="2100">
                ₹65,000
              </data>
              <p className="card-text">Last Month</p>
              <div className="divider card-divider"></div>
              <ul className="revenue-list">
                <li className="revenue-item icon-box">
                  <span className="material-symbols-rounded icon green">
                    trending_up
                  </span>
                  <div>
                    <data className="revenue-item-data" value="15">
                      15%
                    </data>
                    <p className="revenue-item-text">
                      Predicted according to the Planner
                    </p>
                  </div>
                </li>
                <li className="revenue-item icon-box">
                  <span className="material-symbols-rounded icon red">
                    trending_down
                  </span>
                  <div>
                    <data className="revenue-item-data" value="10">
                      10%
                    </data>
                    <p className="revenue-item-text">Prev Month</p>
                  </div>
                </li>
              </ul>
            </div>
          </section>
          <section className="projects">
            <div className="section-title-wrapper">
              <h2 className="section-title">Recent Invesments</h2>
              <button className="btn btn-link icon-box">
                <span>View All</span>
                <span
                  className="material-symbols-rounded icon"
                  aria-hidden="true"
                >
                  arrow_forward
                </span>
              </button>
            </div>
            <ul className="project-list">{/* Repeated list items here */}</ul>
          </section>
          <section className="tasks">
            <div className="section-title-wrapper">
              <h2 className="section-title">Calendar Tasks</h2>
              <button className="btn btn-link icon-box">
                <span>View All</span>
                <span
                  className="material-symbols-rounded icon"
                  aria-hidden="true"
                >
                  arrow_forward
                </span>
              </button>
            </div>
            <ul className="tasks-list">{/* Repeated task items here */}</ul>
            <button className="btn btn-primary" data-load-more>
              <span className="spiner"></span>
              <span>Load More</span>
            </button>
          </section>
        </article>
      </main>
      <footer className="footer">
        <div className="container">
          <ul className="footer-list">
            <li className="footer-item">
              <a href="#" className="footer-link">
                About
              </a>
            </li>
            <li className="footer-item">
              <a href="#" className="footer-link">
                Privacy
              </a>
            </li>
            <li className="footer-item">
              <a href="#" className="footer-link">
                Terms
              </a>
            </li>
            <li className="footer-item">
              <a href="#" className="footer-link">
                Developers
              </a>
            </li>
            <li className="footer-item">
              <a href="#" className="footer-link">
                Support
              </a>
            </li>
            <li className="footer-item">
              <a href="#" className="footer-link">
                Careers
              </a>
            </li>
          </ul>
        </div>
      </footer>
    </div>
  );
};

export default Dashboard;
