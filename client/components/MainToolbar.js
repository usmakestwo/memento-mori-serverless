import React from 'react'
import AppBar from '@material-ui/core/AppBar'
import Typography from '@material-ui/core/Typography'
import Toolbar from '@material-ui/core/Toolbar'
import Button from '@material-ui/core/Button'

const MainToolbar = (props) => (
  <div className={props.classes.root}>
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" color="inherit" className={props.classes.grow}>
          Memento Mori Universitas
        </Typography>
        <Button
          variant="contained"
          color="secondary"
          onClick={props.handleClickOpen}
        >
          Add
        </Button>
      </Toolbar>
    </AppBar>
  </div>
)

export default MainToolbar
