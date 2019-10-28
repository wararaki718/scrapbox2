import React from 'react';

interface Props {}

interface State {
  value: string;
}


class App extends React.PureComponent<Props, State>{
  constructor(props: Props) {
    super(props);
    this.state = {
      value: 'hello'
    };
  }

  render() {
    return (
      <div>
        {this.state.value} world!
      </div>
    );
  }
}

export default App;