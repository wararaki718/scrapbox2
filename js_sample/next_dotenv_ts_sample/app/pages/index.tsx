import React from 'react';

interface Props {}

interface State {
  value: string;
}


class App extends React.PureComponent<Props, State>{
  constructor(props: Props) {
    super(props);
    this.state = {
      value: process.env.MESSAGE // load a environment value
    };
  }

  render() {
    return (
      <div>
        {this.state.value}
      </div>
    );
  }
}

export default App;
