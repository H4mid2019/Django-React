import React from 'react'
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes'

class Article extends React.Component {

  render() {
    return (
      <Router>
      <CustomLayout {...this.props}>
        <BaseRouter/>
      </CustomLayout>
      </Router>
    )
  }
}

export default Article
