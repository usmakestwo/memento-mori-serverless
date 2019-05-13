/* eslint-disable no-underscore-dangle */
import React from 'react'
import Board from 'react-trello'
import PropTypes from 'prop-types'

function DashboardCourses(props) {
  const {
    board,
    isLoading,
    updateRecord,
  } = props

  const onCard = (id, metadata, laneID) => {
    const path = board.lanes.filter(lane => lane.id === laneID)[0].cards
      .filter(card => card.id === id)[0].path
    window.open(path, '_blank')
  }

  const onLane = async (cardId, sourceLaneId, targetLaneId, position, cardDetails) => {
    if (sourceLaneId !== targetLaneId) {
      updateRecord(cardDetails._id.$oid, sourceLaneId, targetLaneId)
    }
  }

  return (
    <React.Fragment>
      { isLoading ? <p>Loading...</p>
        : <Board data={board} draggable onCardClick={onCard} handleDragEnd={onLane} />
    }
    </React.Fragment>
  )
}

DashboardCourses.propTypes = {
  board: PropTypes.array.isRequired,
  isLoading: PropTypes.bool.isRequired,
  updateRecord: PropTypes.func.isRequired,
}

export default DashboardCourses
