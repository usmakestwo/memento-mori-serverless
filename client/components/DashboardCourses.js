import React, { useState } from 'react'
import Board from 'react-trello'
import data from '../api/mock.json'
import mockData from '../api/mock2.json'

const styles = {
  container: {
    padding: 0,
    margin: 0,
    display: 'flex',
    justifyContent: 'space-around',
  },
  flexItem: {
    flex: '1 1 auto',
  },
  card: {
    width: 120,
    marginTop: 10,
    maringBottom: 10,
    cursor: 'pointer',
  }
}

function DashboardCourses() {
  const expensiveComputation = data => {
    const target = { lanes: JSON.parse(data) }
    console.log(target)
    return target
  }
  const boardData = useState( () => expensiveComputation(data) )
  const onCard = (id, metadata, laneID) => {
    console.log(id);
    console.log(metadata);
    console.log(laneID);
  }
  const onLane = (cardId, sourceLaneId, targetLaneId, position, cardDetails) => {
    console.log(cardId);
    console.log(sourceLaneId);
    console.log(targetLaneId);
    console.log(position);
    console.log(cardDetails);
  }
  return (
    <Board data={boardData[0]} draggable onCardClick={onCard} handleDragEnd={onLane} />
  )
}

export default DashboardCourses
