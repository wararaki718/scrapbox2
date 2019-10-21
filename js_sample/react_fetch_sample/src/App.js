import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      username: '',
      location: '',
      create_at: ''
    };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    const self = this;
    fetch('https://api.github.com/users/wararaki')
      .then(response => response.json())
      .then(jsonData => {
        self.setState({
          value: String(Date.now()),
          username: jsonData.login,
          location: jsonData.location,
          create_at: jsonData.create_at
        })
      });
  }

  // one render
  render () {
    return (
      <div>
        <div>
          <button onClick={this.handleClick}>
            click
          </button>
        </div>
        <div>
          AccesssTime: {this.state.value}
        </div>
        <div>
          Username: {this.state.username}
        </div>
        <div>
          Location: {this.state.location}
        </div>
        <div>
          CreateAt: {this.state.create_at}
        </div>
      </div>
    );
  }
}

export default App;
