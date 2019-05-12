import React, { useState, useEffect } from 'react'
import Board from 'react-trello'
import { fetchRecord, updateRecord } from '../api/courses'
import PropTypes from 'prop-types'

function DashboardCourses() {
  const [isLoading, setIsLoading] = useState(true);
  const [board, setBoard] = useState([]);

  // Fetch todos from API
  const fetchData = async () => {
    setIsLoading(true)
    const result = await fetchRecord()
    setBoard({ lanes: JSON.parse(result) })
    setIsLoading(false)
  }

  // Call Todos on load
  useEffect(() => {
    fetchData()
  }, [])

  const onCard = (id, metadata, laneID) => {
    let path = board.lanes.filter(lane => lane.id === laneID)[0].cards
      .filter(card => card.id === id)[0].path
    window.open(path, "_blank")
  }

  const onLane = async (cardId, sourceLaneId, targetLaneId, position, cardDetails) => {
    if (sourceLaneId !== targetLaneId) {
      const result = await updateRecord(cardDetails._id["$oid"], sourceLaneId, targetLaneId)
      fetchData()
    }
  }

  return (
    <React.Fragment>
    { isLoading ? <p>Loading...</p> :
      <Board data={board} draggable onCardClick={onCard} handleDragEnd={onLane} />
    }
    </React.Fragment>
  )
}

DashboardCourses.propTypes = {
  board: PropTypes.array.isRequired,
}

export default DashboardCourses
