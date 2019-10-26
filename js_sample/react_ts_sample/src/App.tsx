import React from 'react';
import './App.css';

interface Props {
}

interface State {
  name: string
}

export class App extends React.PureComponent<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {name: 'typescript'}
  }

  render() {
    return (
      <div>hello, {this.state.name}!!</div>
    )
  }
}

export default App;
