-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2022 at 07:59 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `job`
--

-- --------------------------------------------------------

--
-- Table structure for table `applyjob`
--

CREATE TABLE `applyjob` (
  `Aid` int(11) NOT NULL,
  `Uid` int(11) NOT NULL,
  `Jid` int(11) NOT NULL,
  `Cid` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `sector` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applyjob`
--

INSERT INTO `applyjob` (`Aid`, `Uid`, `Jid`, `Cid`, `username`, `Status`, `title`, `sector`, `type`) VALUES
(2, 1, 1, 3, 'Muhammad Zulfiqar Khan', 'Approved (Shortlist)', 'Teacher required for CS Department - AI/Networking', 'Education', 'Online');

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

CREATE TABLE `contactus` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `details` varchar(255) NOT NULL,
  `addationaldetails` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contactus`
--

INSERT INTO `contactus` (`id`, `fname`, `lname`, `email`, `details`, `addationaldetails`) VALUES
(15, 'Hamza', 'khan', 'hamza@gmail', 'Abdullah', 'demo');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `Jid` int(11) NOT NULL,
  `Cid` int(11) NOT NULL,
  `Sector` varchar(255) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `Description` longtext NOT NULL,
  `Experience` longtext NOT NULL,
  `Type` varchar(100) NOT NULL,
  `Benefit` longtext NOT NULL,
  `Salary` varchar(1000) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`Jid`, `Cid`, `Sector`, `Title`, `Description`, `Experience`, `Type`, `Benefit`, `Salary`, `Status`) VALUES
(1, 3, 'Education', 'Teacher required for CS Department - AI/Networking', 'Testing des.', '1', 'Online', 'Hello', '150000', 'Active'),
(2, 3, 'Property and Construction', 'Need Marketing Person', 'Multi-National Comany', '2', 'Office Base', 'All Allownss', '75000', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `resume`
--

CREATE TABLE `resume` (
  `Rid` int(11) NOT NULL,
  `Uid` int(11) NOT NULL,
  `Deg1` varchar(255) NOT NULL,
  `Pas1` varchar(255) NOT NULL,
  `Sat1` varchar(255) NOT NULL,
  `Deg2` varchar(255) NOT NULL,
  `Pas2` varchar(255) NOT NULL,
  `Sat2` varchar(255) NOT NULL,
  `Deg3` varchar(255) NOT NULL,
  `Pas3` varchar(255) NOT NULL,
  `Sat3` varchar(255) NOT NULL,
  `Deg4` varchar(255) NOT NULL,
  `Pas4` varchar(255) NOT NULL,
  `Sat4` varchar(255) NOT NULL,
  `Deg5` varchar(255) NOT NULL,
  `Pas5` varchar(255) NOT NULL,
  `Sat5` varchar(255) NOT NULL,
  `Comp1` varchar(255) NOT NULL,
  `Des1` varchar(255) NOT NULL,
  `start1` varchar(255) NOT NULL,
  `end1` varchar(255) NOT NULL,
  `Comp2` varchar(255) NOT NULL,
  `Des2` varchar(255) NOT NULL,
  `start2` varchar(255) NOT NULL,
  `end2` varchar(255) NOT NULL,
  `Comp3` varchar(255) NOT NULL,
  `Des3` varchar(255) NOT NULL,
  `start3` varchar(255) NOT NULL,
  `end3` varchar(255) NOT NULL,
  `Cert1` varchar(255) NOT NULL,
  `Title1` varchar(255) NOT NULL,
  `cstart1` varchar(255) NOT NULL,
  `cend1` varchar(255) NOT NULL,
  `Cert2` varchar(255) NOT NULL,
  `Title2` varchar(255) NOT NULL,
  `cstart2` varchar(255) NOT NULL,
  `cend2` varchar(255) NOT NULL,
  `Cert3` varchar(255) NOT NULL,
  `Title3` varchar(255) NOT NULL,
  `cstart3` varchar(255) NOT NULL,
  `cend3` varchar(255) NOT NULL,
  `skill1` varchar(255) NOT NULL,
  `level1` varchar(255) NOT NULL,
  `skill2` varchar(255) NOT NULL,
  `level2` varchar(255) NOT NULL,
  `skill3` varchar(255) NOT NULL,
  `level3` varchar(255) NOT NULL,
  `language1` varchar(255) NOT NULL,
  `llevel1` varchar(255) NOT NULL,
  `language2` varchar(255) NOT NULL,
  `llevel2` varchar(255) NOT NULL,
  `language3` varchar(255) NOT NULL,
  `llevel3` varchar(255) NOT NULL,
  `job` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resume`
--

INSERT INTO `resume` (`Rid`, `Uid`, `Deg1`, `Pas1`, `Sat1`, `Deg2`, `Pas2`, `Sat2`, `Deg3`, `Pas3`, `Sat3`, `Deg4`, `Pas4`, `Sat4`, `Deg5`, `Pas5`, `Sat5`, `Comp1`, `Des1`, `start1`, `end1`, `Comp2`, `Des2`, `start2`, `end2`, `Comp3`, `Des3`, `start3`, `end3`, `Cert1`, `Title1`, `cstart1`, `cend1`, `Cert2`, `Title2`, `cstart2`, `cend2`, `Cert3`, `Title3`, `cstart3`, `cend3`, `skill1`, `level1`, `skill2`, `level2`, `skill3`, `level3`, `language1`, `llevel1`, `language2`, `llevel2`, `language3`, `llevel3`, `job`) VALUES
(7, 1, 'Master', '2022-10-22', 'Completed', 'Baheclor', '2022-10-22', 'Completed', 'FSC/FCS', '2022-10-22', 'Completed', 'Matric', '2022-10-22', 'Completed', 'Midle', '2022-10-22', 'Completed', 'CUI', 'Developer', '2022-10-22', '2022-10-22', 'ACME', 'Developer', '2022-10-22', '2022-10-22', 'CANE', 'Developer', '2022-10-22', '2022-10-22', 'IBM', 'Cybersecurity', '2022-10-22', '2022-10-22', 'Google', 'Techinical', '2022-10-22', '2022-10-22', 'Coursera', 'Machine', '2022-10-22', '2022-10-22', 'Laravel', 'Expert', 'PHP', 'Expert', 'Django', 'Expert', 'English', 'Native', 'French', 'Fluent', 'Urdu', 'Professional', 'Education');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Uid` int(11) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Cnic` varchar(255) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Postalcode` varchar(255) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Uid`, `Fname`, `Lname`, `Cnic`, `Gender`, `Email`, `Phone`, `Address`, `Postalcode`, `Password`, `Type`) VALUES
(1, 'Muhammad Zulfiqar', 'Khan', '3740607766041', 'Male', 'khan@gmail.com', '03445055537', 'wah cantt, pof', '', 'zulfiqar', 2),
(2, 'Sytem', 'Admin', '0000000000', 'Male', 'systemadmin@gmail.com', '0000000000', 'none', '', 'systemadmin', 1),
(3, 'NetSol Pvt Ltd.', 'Fahad Bin Shekih', 'IT Company', '', 'info@netsol.pk', '051-097861', 'F-9 Islamabad', 'Active', 'netsol', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applyjob`
--
ALTER TABLE `applyjob`
  ADD PRIMARY KEY (`Aid`);

--
-- Indexes for table `contactus`
--
ALTER TABLE `contactus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`Jid`);

--
-- Indexes for table `resume`
--
ALTER TABLE `resume`
  ADD PRIMARY KEY (`Rid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`Uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applyjob`
--
ALTER TABLE `applyjob`
  MODIFY `Aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `contactus`
--
ALTER TABLE `contactus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `Jid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `resume`
--
ALTER TABLE `resume`
  MODIFY `Rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `Uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
