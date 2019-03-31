import React, { useState, useEffect } from 'react'
import Head from 'next/head'
import Button from '@material-ui/core/Button'
import Grid from '@material-ui/core/Grid'
import AppBar from '@material-ui/core/AppBar'
import Typography from '@material-ui/core/Typography'
import Toolbar from '@material-ui/core/Toolbar'
import Courses from '../components/courses'
import CircularProgress from '@material-ui/core/CircularProgress';
import courseAPI from '../api/courses'

function IndexPage(props) {
  const [courses, setCourses] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const fetchData = async () => {
    setIsLoading(true)
    const results = JSON.parse(await courseAPI())
    setCourses(results)
    setIsLoading(false)
  }
  useEffect(() => {
    if (!courses.length) {
      fetchData()
    }
  }, [])
  return (
    <div>
        <Head>
          <title>My page title</title>
          <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        </Head>
        <Grid container spacing={24}>
          <AppBar position="static">
            <Toolbar>
              <Typography variant="h6" color="inherit">
                Memento Mori Universitas
              </Typography>
            </Toolbar>
          </AppBar>
          <Grid item xs={12}>
            { isLoading ? <CircularProgress /> :
              <div>
                {courses.map(course =>
                  <Courses
                    key={course._id["$oid"]}
                    title={course.name}
                    description={course.description}
                  />)
                }
              </div>
            }
          </Grid>
        </Grid>
    </div>
  )
}

export default IndexPage
