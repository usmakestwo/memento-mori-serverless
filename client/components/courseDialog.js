import React from 'react'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import Dialog from '@material-ui/core/Dialog'
import DialogActions from '@material-ui/core/DialogActions'
import DialogContent from '@material-ui/core/DialogContent'
import DialogContentText from '@material-ui/core/DialogContentText'
import DialogTitle from '@material-ui/core/DialogTitle'

function CourseDialog(props){
  return (
    <div>
        <Dialog
          open={props.open}
          onClose={props.handleClose}
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
            />
            <TextField
              autoFocus
              margin="dense"
              id="description"
              label="Description"
              type="text"
              fullWidth
            />
          </DialogContent>
          <DialogActions>
            <Button color="primary">
              Create
            </Button>
            <Button onClick={props.handleClose} color="primary">
              Cancel
            </Button>
          </DialogActions>
        </Dialog>
      </div>
  )
}

export default CourseDialog
