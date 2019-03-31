import React from 'react'
import PropTypes from 'prop-types'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemIcon from '@material-ui/core/ListItemIcon'
import IconButton from '@material-ui/core/IconButton'
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction'
import ListItemText from '@material-ui/core/ListItemText'
import FolderIcon from '@material-ui/icons/Folder'
import CloudIcon from '@material-ui/icons/Cloud'
import VisibilityIcon from '@material-ui/icons/Visibility'

function Courses(props) {
  const { title, description } = props
  return (
    <List dense={true}>
      <ListItem>
        <ListItemIcon>
          <FolderIcon />
        </ListItemIcon>
        <ListItemText
          primary={title}
          secondary={description}
        />
        <ListItemSecondaryAction>
          <IconButton>
            <CloudIcon />
          </IconButton>
          <IconButton>
            <VisibilityIcon />
          </IconButton>
        </ListItemSecondaryAction>
      </ListItem>
    </List>
  )
}

Courses.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired
}

export default Courses