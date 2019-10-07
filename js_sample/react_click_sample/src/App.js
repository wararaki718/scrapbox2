import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isFlag: true};
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      isFlag: !state.isFlag
    }));
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
          {this.state.isFlag ? 'Hello': 'World'}
        </div>
      </div>
    );
  }
}

export default App;
