import React from 'react'
import PropTypes from 'prop-types'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemIcon from '@material-ui/core/ListItemIcon'
import IconButton from '@material-ui/core/IconButton'
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction'
import ListItemText from '@material-ui/core/ListItemText'
import Link from '@material-ui/core/Link'
import FolderIcon from '@material-ui/icons/Folder'
import LockIcon from '@material-ui/icons/Lock'
import LockOpenIcon from '@material-ui/icons/LockOpen'
import CloudIcon from '@material-ui/icons/Cloud'

function ListCourses(props) {
  const {
    title,
    description,
    path,
    addToPin,
    id,
    favorite
  } = props
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
            <Link href={path} target="_blank" rel="noopener">
              <CloudIcon />
            </Link>
          </IconButton>
          <IconButton onClick={() => addToPin(id)}>
            { favorite ? <LockIcon /> : <LockOpenIcon /> }
          </IconButton>
        </ListItemSecondaryAction>
      </ListItem>
    </List>
  )
}

ListCourses.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired
}

export default ListCourses