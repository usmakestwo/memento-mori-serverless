import React, { useState } from 'react'
import Board from 'react-trello'
import data from '../api/mock.json'
import PropTypes from 'prop-types'

function DashboardCourses() {
  const expensiveComputation = data => {
    const target = { lanes: JSON.parse(data) }
    console.log(target)
    return target
  }
  const boardData = useState( () => expensiveComputation(data) )
  const onCard = (id, metadata, laneID) => {
    let path = boardData[0].lanes.filter(lane => lane.id === laneID)[0].cards.filter(card => card.id === id)[0].path
    window.open(path, "_blank")
  }
  const onLane = (cardId, sourceLaneId, targetLaneId, position, cardDetails) => {
    console.log(`Updating id: ${cardDetails._id["$oid"]} to source ${targetLaneId}`)
  }
  return (
    <Board data={boardData[0]} draggable onCardClick={onCard} handleDragEnd={onLane} />
  )
}

DashboardCourses.propTypes = {
  boardData: PropTypes.array.isRequired,
}

export default DashboardCourses
