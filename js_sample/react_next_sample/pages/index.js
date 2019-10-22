import React from 'react'

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: '', username: ''};

    // bind modules
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    const self = this;
    fetch('https://api.github.com/users/wararaki')
      .then(response => response.json())
      .then(jsonData => {
        self.setState({
          value: String(Date.now()),
          username: jsonData.login
        })
      });
  }

  render() {
    return (
      <div>
        <div>
          <button onClick={this.handleClick}>
            click
          </button>
        </div>
        <div>
          AccessTime: {this.state.value}
        </div>
        <div>
          Username: {this.state.username}
        </div>
      </div>
    );
  }
}

export default Home
