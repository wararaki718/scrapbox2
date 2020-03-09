import React from 'react'

class SamplePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {message: '', reply: ''};
    
    this.handleChange = this.handleChange.bind(this);
    this.messageSend = this.messageSend.bind(this);
  }

  handleChange(event) {
    this.setState({message: event.target.value});
  }

  messageSend(){
    const self = this;
    const current_date = new Date();
    
    // send message
    fetch(
      'http://localhost:8080/message',
      {
        method: 'POST',
        mode: 'cors',
        headers: {
          "Content-Type": "application/json; charset=utf-8"
        },
        body: JSON.stringify({
          content: self.state.message,
          requestTime: current_date.toString()
        })
      })
      .then(response => response.json())
      .then(data => {
        self.setState({
          message: '',
          reply: data.content + " " + data.responseTime
        })
      });
  }

  render() {
    return (
      <div>
        <div>
          <form>
            <input type="text" value={this.state.message} onChange={this.handleChange} />
          </form>
          <button onClick={this.messageSend}>send message</button>
        </div>
        <div>
          {this.state.reply}
        </div>
      </div>
    )
  }
}

export default SamplePage
