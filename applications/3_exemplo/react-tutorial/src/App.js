import React, { Component } from 'react'
import Table from './Table'

class App extends Component {
  // 1. We move the initial data array into the component's state
  state = {
    characters: [
      {
        name: 'Charlie',
        job: 'Janitor',
      },
      {
        name: 'Mac',
        job: 'Bouncer',
      },
      {
        name: 'Dee',
        job: 'Aspring actress',
      },
      {
        name: 'Dennis',
        job: 'Bartender',
      },
    ],
  }

  // 2. This method sits on the class level, completely separate from render()
  removeCharacter = (index) => {
    const { characters } = this.state
    
    this.setState({
      characters: characters.filter((character, i) => {
        return i !== index
      }),
    })
  }

  // 3. render() now only has ONE variable named 'characters' pulled from state
  render() {
    const { characters } = this.state

    return (
      <div className="container">
        <Table characterData={characters} removeCharacter={this.removeCharacter} />
      </div>
    )
  }
}

export default App