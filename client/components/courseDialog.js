import React from 'react'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import Dialog from '@material-ui/core/Dialog'
import DialogActions from '@material-ui/core/DialogActions'
import DialogContent from '@material-ui/core/DialogContent'
import DialogContentText from '@material-ui/core/DialogContentText'
import DialogTitle from '@material-ui/core/DialogTitle'

function CourseDialog(props){
  const { open, handleClose, createCourse } = props
  return (
    <div>
        <Dialog
          open={open}
          onClose={handleClose}
        >
          <DialogTitle id="form-dialog-title">Add Course</DialogTitle>
          <DialogContent>
            <DialogContentText>
              What subject would you like to learn next?
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="name"
              label="Name"
              type="text"
              fullWidth
              placeholder="Learning..."
            />
            <TextField
              margin="dense"
              id="description"
              label="Description"
              type="text"
              fullWidth
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={() => createCourse(event)} color="primary">
              Create
            </Button>
            <Button onClick={handleClose} color="primary">
              Cancel
            </Button>
          </DialogActions>
        </Dialog>
      </div>
  )
}

export default CourseDialog
