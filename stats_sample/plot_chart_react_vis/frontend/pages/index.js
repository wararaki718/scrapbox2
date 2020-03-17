import React from 'react';
import styled from 'styled-components';
import {XYPlot, LineSeries} from 'react-vis';

const PlotArea = styled.div`
  padding: 5px 10px;
`;


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [
        {x: 0, y: 8},
        {x: 1, y: 5},
        {x: 2, y: 4},
        {x: 3, y: 9},
        {x: 4, y: 1},
        {x: 5, y: 7},
        {x: 6, y: 6},
        {x: 7, y: 3},
        {x: 8, y: 2},
        {x: 9, y: 0}
      ]
    };

    this.getData = this.getData.bind(this);
  }

  getData() {
    const self = this;
    fetch('http://localhost:8000/aggs', {
      method: 'GET',
      mode: 'cors',
      credentials: 'same-origin',
      referrer: 'no-referrer'
    })
      .then(response => response.json())
      .then(jsonData => {
        self.setState({
          data: jsonData.data
        })
      });
  }

  render() {
    return (
      <div>
        <div>
          <button onClick={this.getData}>
            click
          </button>
        </div>
        <div className="PlotArea">
          <XYPlot height={300} width={300}>
            <LineSeries data={this.state.data} />
          </XYPlot>
        </div>
      </div>
    );
  }
}

export default App;
