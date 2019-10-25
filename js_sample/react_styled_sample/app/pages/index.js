import React from 'react';
import styled from 'styled-components';

const Button = styled.button`
  padding: 5px 10px;
  color: blue;
`;

const ResultDiv = styled.div`
  padding: 5px 10px;
  font-size: 20px;
`;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {flag: true};

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    const flag = this.state.flag;
    this.setState({
      flag: !flag
    });
  }

  render() {
    return (
      <div>
        <div>
          <Button onClick={this.handleClick}>hello</Button>
        </div>
        <ResultDiv>
          {this.state.flag? 'Hello': 'World'}
        </ResultDiv>
      </div>
    )
  }
}

export default App
