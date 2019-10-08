import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: '', output: ''};

    // bind function
    this.handleClick = this.handleClick.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleClick(event) {
    this.setState(state => ({output: state.value}));
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  render() {
    return (
      <div className="app-layout">
        <div className="form-layout">
          <form>
            <label>Input: <input type="text" value={this.state.value} onChange={this.handleChange} /></label>
          </form>
          <input type="button" value="Show" onClick={this.handleClick}/>
        </div>
        <div className="output-layout">
          {this.state.output}
        </div>
      </div>
    );
  }
}

export default App;
