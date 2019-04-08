import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import Head from 'next/head'
import Button from '@material-ui/core/Button'
import Grid from '@material-ui/core/Grid'
import AppBar from '@material-ui/core/AppBar'
import Typography from '@material-ui/core/Typography'
import Toolbar from '@material-ui/core/Toolbar'
import ListCourses from '../components/listCourses'
import CourseDialog from '../components/courseDialog'
import CircularProgress from '@material-ui/core/CircularProgress';
import courseAPI from '../api/courses'

const styles = {
  root: {
    flexGrow: 1,
  },
  grow: {
    flexGrow: 1,
  },
};

function IndexPage(props) {
  const { classes } = props
  const [courses, setCourses] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [open, setOpen] = useState(false)
  const fetchData = async () => {
    setIsLoading(true)
    // const results = JSON.parse(await courseAPI())
    const results = JSON.parse("[{\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d7\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning Cooking\", \"description\": \"Learning how to cook\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-cooking\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d9\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning Python\", \"description\": \"Learning Python\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-python\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d3\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning MySQL\", \"description\": \"Learning SQL best practices\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-mysql\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64e0\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning fitness\", \"description\": \"Tips and tools for a healthier body and nutrition\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-fitness\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64dc\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning Game Dev\", \"description\": \"Learning game development with Unity\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-game-dev\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d4\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning Statistics\", \"description\": \"Learning statistics\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-statistics\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64dd\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning to Play the Piano\", \"description\": \"Learning how to play the piano\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-to-play-the-piano\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64e2\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning bash\", \"description\": \"Learning bash to automate everyday tasks\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-bash\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64e4\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning React Native\", \"description\": \"Building mobile application with React\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-react-native\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d8\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning GCP\", \"description\": \"Learning how to use GCP and Terraform for analytics\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-gcp\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d6\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning Contentful\", \"description\": \"Learning how to use Contentful with ReactJS\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-contentful\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64df\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning algorithms\", \"description\": \"Learning common algorithm and how to design one\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-algorithms\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64da\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning GraphQL\", \"description\": \"Learning GraphQL\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-graphql\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d5\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning next.js\", \"description\": \"Learning next.js\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-next.js\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64de\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning algebra\", \"description\": \"Learning alegrabra for statistics\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-algebra\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64e1\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning hacking\", \"description\": \"Learning ethical hacking\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-hacking\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64d2\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning French\", \"description\": \"Learning basic conversational french\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-french\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64db\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning C Sharp\", \"description\": \"Learning C# for gaming and mobile development\", \"uploaded\": true, \"path\": \"https://github.com/memento-mori-universitas/learning-c-sharp\"}, {\"_id\": {\"$oid\": \"5c8eaaa2246320a756ef64e3\"}, \"createdAt\": {\"$date\": 1552839266802}, \"name\": \"Learning Vim\", \"description\": \"Learning how to use vim proficiently\", \"uploaded\": true}]")
    setCourses(results)
    setIsLoading(false)
  }
  useEffect(() => {
    if (!courses.length) {
      fetchData()
    }
  }, [])
  const handleClickOpen = () => {
    setOpen(true);
  }

  const handleClose = () => {
    setOpen(false);
  }
  return (
    <div>
        <Head>
          <title>Memento Mori Universitas</title>
          <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        </Head>
        <Grid container spacing={24}>
          <div className={classes.root}>
            <AppBar position="static">
              <Toolbar>
                <Typography variant="h6" color="inherit" className={classes.grow}>
                  Memento Mori Universitas
                </Typography>
                <Button
                  variant="contained"
                  color="secondary"
                  onClick={handleClickOpen}
                >
                  Add
                </Button>
              </Toolbar>
            </AppBar>
          </div>
          <Grid item xs={12}>
            { isLoading ? <CircularProgress /> :
              <div>
                {courses.map(course =>
                  <ListCourses
                    key={course._id["$oid"]}
                    title={course.name}
                    description={course.description}
                    path={course.path}
                  />)
                }
              </div>
            }
          </Grid>
          <CourseDialog open={open} handleClose={handleClose}/>
        </Grid>
    </div>
  )
}


IndexPage.propTypes = {
  classes: PropTypes.object.isRequired,
}

export default withStyles(styles)(IndexPage);
