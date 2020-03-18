import React from 'react';
import styled from 'styled-components';

const MessageColor = styled.div`
  padding: 5px 10px;
  color: blue;
`;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: process.env.MESSAGE
    };
  }

  render() {
    return (
      <div>
        <h3 className="MessageColor">{this.state.message}</h3>
      </div>
    );
  }
}

export default App;
